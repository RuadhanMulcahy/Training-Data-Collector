from flags import flags
import sys

def get_input():
    args = sys.argv
    arg_len = len(args)

    if arg_len % 2 != 1:
        raise Exception("Invalid command line arguments.")

    index = 1
    while index < arg_len:
        if args[index] == '--username':
            flags['username'] = args[index+1]
            index += 1
        elif args[index] == '--game_id':
            flags['game_id'] = args[index+1]
            index += 1
        elif args[index] == '--highlight':
            if args[index+1] == 'True':
                flags['highlight'] = True
            else:
                flags['highlight'] = False
            index += 1
        elif args[index] == '--train_or_val':
            flags['train_or_val'] = args[index+1]
            index += 1
        elif args[index] == '--style':
            flags['board_style'] = args[index+1]
            index += 1
        else:
            raise Exception(f"{args[index]} is not a valid argument.")
        index+=1

    if flags['username'] == '':
        raise Exception(f"{args[index]} is not a valid argument.")