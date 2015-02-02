#! /usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize
import os
import codecs
import re
from Canvas import Line
from distutils.tests.setuptools_build_ext import if_dl

class ExceptionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#end class ExceptionError()


def ReadFile(valid_content, source_dir, result_dir, file_name):
    line_num = 1
    full_dir_path = source_dir + file_name
    
    
    with codecs.open(full_dir_path, 'r', 'utf8') as input_file:
        line = input_file.readline() #read this line
        title = ''
        
        while line:
            
            jump_this_line = False
            create_new_file = False
            end_file = False
            title_index = line.find('title=\"')            
            
            #(1) get title
            if title_index > 0:
                title = line[title_index+7:-3]
                line = title
                print '@target: ' + title
                create_new_file = True
            #end if not title :<doc ....>    
            
            #(2) 過濾label下面的重複條目
            if line == title: #if this line only has one word which is the same as <title>, ignore it!
                print '@filter <same_as_title>'
                jump_this_line = True
            #end if
            
            #(3) 過濾單行只有空白, tab跟換行的字串
            if len(line.split('\n')) < 2: # this line is consist of space, line-enter and tab 
                print '@filter <space/tab/enter>'
                jump_this_line = True
            #end this line is consist of space, line-enter and tab
            
            if line == '</doc>' :
                #jump_this_line = True
                end_file = True
            #end writing file   
            
            if  not jump_this_line:
                if not end_file:
                    if create_new_file:
                        with codecs.open(result_dir+title+'.txt', 'w', 'utf8') as outputfile:
                            print '@@line stored: ' + line
                            
                            jump_this_line = False   
                            '''
                            sentences = sent.tokenize(line)
                            for s in sentences:
                                outputfile.write(s)
                            '''
                    #end newfile
                    else: #don't create new file
                        
                        with codecs.open(result_dir+title+'.txt', 'a', 'utf8') as outputfile:
                            print '@@line stored: ' + line                        
                            jump_this_line = False   
                            
                            sentences = sent_tokenize(line)
                            for s in sentences:
                                outputfile.write(s)
                        #end with
                    #end create new file
                #endif endflie
                else: #endfile
                    outputfile.close()
                #end                             
            #end if not jump line & not end    
   
            line = input_file.readline()
            jump_this_line = False
            end_file = False
            create_new_file = False
            line_num = line_num + 1
        
            if line_num == 115:
                break
            
        #end while
        jump_this_line = False
        print '///////////////'
        print valid_content[0:50]
        #return valid_content
        input_file.close()
    #end with
#end ReadFile()


def main(source_dir, result_dir, file_name):
    print '@Parsing sentences... '
    try:
        valid_content = []
        
        file_content_segment = []
        sentence_list = []
        ReadFile(valid_content, source_dir, result_dir, file_name)
        #input_file = open(full_dir_path, "r")
        #file_content_segment = ReadFile(full_dir_path)
        print 'hi in main'
        print '---------------------'
        
        for sub in valid_content:
            print '# : ' + sub[:-1]
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
    
    root_dir = 'E:\MyGit\CloneGit\wiki_en_tokenizer\\'
    
    #read text file from the original directory, and replace all unicode characters
    source_dir = 'C:\Users\kame169\Desktop\\'
    
    #output the sliced sentences
    result_dir = 'E:\MyGit\CloneGit\wiki_en_tokenizer\\result\\'
    print 'hi in out'
    main(source_dir, result_dir, 'wiki_00')
    
    '''
    test = 'aaa.'
    test2 = ['aaa', 'bbb', 'ccc']
    test = test.split('.')
    print '@r :' + str(test)
    print len(test)
    #print str(test2)
    '''

    
#end for
#end if
