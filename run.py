import argparse
import os
import subprocess

root = os.path.abspath(os.path.dirname(__file__))

parser = argparse.ArgumentParser(description="Config the SHMS Application")
parser.add_argument('-e', '--env', metavar='env', type=str, help='The env path', default='./.env')

args = parser.parse_args()
env_path = args.env

gunicorn_virtual_env = os.path.join(env_path, 'bin/gunicorn')


def main():
    p = subprocess.Popen((gunicorn_virtual_env, '--reload', 'shms.app:get_app()'))
    try:
        print('Starting server with: {}'.format(gunicorn_virtual_env))
        p.wait()
    except KeyboardInterrupt:
        try:
            p.terminate()
        except OSError:
            pass
        p.wait()


if __name__ == '__main__':
    main()
