# __name__と__main__
import lesson68_package.talk.animal

import config

# importされたときに読み込まれないようにするため
def main():
    lesson68_package.talk.animal.sing()

if __name__ == '__main__':
    main()


print('lesson:', __name__)