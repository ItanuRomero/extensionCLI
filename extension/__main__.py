import sys
from .search_handler import search, bring_summary
from icecream import ic


def main():
    ic('Extension CLI started')
    args = sys.argv[1:]
    ic('The args called: ', args)
    if len(args) == 1:
        ic('Searching for the file extension...')
        value_returned = search(args[0])
        ic('Interpreting summary of the search...')
        summary = bring_summary(value_returned[0])
        ic('Here there is:')
        print(summary)

if __name__ == '__main__':
    main()
