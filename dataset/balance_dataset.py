from file import *
import random

amount_of_validation_data = 0.15 #%
train_folders_way = 'train/'
valid_folders_way = 'valid/'
#train_folders_way = 'valid/'
#valid_folders_way = 'test/'

if __name__ == "__main__":
    for folder in os.listdir(train_folders_way):
        try:
            os.mkdir(valid_folders_way + folder)
        except Exception as ex:
            #print(er)
            pass
        
        output_folder_way = train_folders_way + folder
        input_folder_way = valid_folders_way + folder

        output_folder = Folder(output_folder_way)
        input_folder  = Folder(input_folder_way)
        names = output_folder.get_sorted_files()
        count_of_files = len(names)
        print(folder + ": " + str(count_of_files))
        amount_of_files_to_move = amount_of_validation_data * count_of_files
        print(folder + ": " + str(amount_of_files_to_move))
        random.shuffle(names)
        files_to_move = names[:int(amount_of_files_to_move)]
        for target in files_to_move:
            source = output_folder_way + '/' + target
            destination =  input_folder_way + '/' + target
            shutil.move(source, destination)
            #print(source)
