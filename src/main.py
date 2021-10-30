from .arguments import get_args
from .api import extract_link_info, get_favorites


def main():
    args = get_args()

    if args['favorite_users']:
        get_favorites('artist')

    if args['favorite_posts']:
        get_favorites('post')

    for link in args['links']:
        if not extract_link_info(link):
            print('[Error] Invalid link: {}'.format(link))

    for link in args['fromfile']:
        if not extract_link_info(link):
            print('[Error] Invalid link: {}'.format(link))

    print('Done.')
