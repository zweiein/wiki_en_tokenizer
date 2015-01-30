#! /usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize
import os
import codecs
import re

class ExceptionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#end class ExceptionError()


def ReadFile(full_dir_path):
    count = 0
    with codecs.open(full_dir_path, 'r', 'utf8') as input_file:
        line = input_file.readline() #read this line
        
        while line:
            title_index = line.find("title=\"")
            
            if title_index != 0:
                title = line[title_index:-2]
                print title
            
            line = input_file.readline()
            count = count + 1
            
            if count == 20000:
                break
#end while
#return file_content_segment
#end ReadFile()


def main(result_dir, file_name):
    print '@Parsing sentences... '
    try:
        full_dir_path = replaced_dir + file_name
        print '@PATH : ' + full_dir_path
        
        file_content_segment = []
        sentence_list = []
        
        #input_file = open(full_dir_path, "r")
        #file_content_segment = ReadFile(full_dir_path)
        
        ReadFile(full_dir_path)
        '''
            # write results into text files
            with codecs.open( result_dir + text_name, 'w', 'utf8' ) as output_file:
            for sub_sent in current_documents:
            #sentences tokenize
            sub_sent_tokenize = sent_tokenize(str(sub_sent))
            
            for sent in sub_sent_tokenize:
            if len(sent) < 1:
            j = j + 1
            print '## : ' + sent
            else:
            output_file.write(sent)
            output_file.write('\n')
            output_file.close()
            #end with
            input_file.close()
            print '@Write file success!\n'
            #end try
            '''
    except ExceptionError as e:
        print '[Error] ' + e + '\n@Cb current_file : ' + text_name
#end main()



if __name__ == '__main__':
    
    root_dir = '/Users/slp/Desktop/parse_wiki_en'
    
    #read text file from the original directory, and replace all unicode characters
    source_dir = '/Users/slp/Download/'
    
    #output the sliced sentences
    result_dir = '/Users/slp/Desktop/parse_wiki_en/result/'
    
    main(result_dir, 'wiki_00')
#end for
#end if
