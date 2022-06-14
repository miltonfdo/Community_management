
import csv
import pandas as pd
from tabulate import tabulate



#Function to read the number of appartments and occupancy
def getCommunityDetails():
    with open('Blocks.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["Blocks"]} {row["BHK"]} {row["TotalAppartments"]} {row["TotalOccupied"]} {row["TotalUnoccupied"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

        pd.options.display.max_rows = 9999

        df = pd.read_csv('Blocks.csv')
        #print(df) 
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))



        #file is empty getting input from user to update the csv file
        if line_count == 0:
            with open('Blocks.csv', mode='w') as csv_file:

                #Blocks,BHK,TotalAppartments,TotalOccupied,TotalUnoccupied
                Blocks=0
                BHK=1
                maxBHK=0
                TotalAppartment=0
                TotalOccupied=0 
                TotalUnoccupied=0
                
                
                Blocks = int(input("Total number of Blocks in community:"))
                fieldnames = ['Blocks','BHK','TotalAppartments','TotalOccupied','TotalUnoccupied']
                Blocks_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                Blocks_writer.writeheader()

                for block in range(Blocks):
                   
                    print("what is the maximum BHK in Block ",str(block+1))
                    maxBHK=int(input ("Example- 3:  "))
                    for bhk in range(maxBHK):
                      
                        print("Total Number of ",str(bhk+1),"BHK in Block ",str(block+1)," :")
                        TotalAppartment=int(input ("Example - 2:  "))

                        print("Total Number of ",str(bhk+1),"BHK Occupied in Block ",str(block+1),":")
                        TotalOccupied=int(input (" :"))
                        
                        TotalUnoccupied=TotalAppartment-TotalOccupied

                        Blocks_writer.writerow({'Blocks':block+1,'BHK':bhk+1,'TotalAppartments':TotalAppartment,'TotalOccupied':TotalOccupied,'TotalUnoccupied':TotalUnoccupied})




getCommunityDetails()
