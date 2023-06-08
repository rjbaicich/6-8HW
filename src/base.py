import pandas as pd

class Base:
    def __init__(self):
        self.df = None
        self.csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\6-8HW\dohmh-beach-water-quality-data-1.csv'
        self.get_data()
        self.clean_data()
        
    def return_string(self):
        return self.csv_file
        
    def get_data(self):
        self.df = pd.read_csv(self.csv_file)
        return self.df
    
    def clean_data(self):
    
        #Remove duplicates
        self.df.drop_duplicates(inplace=True)
        
        #Handle missing values
        self.df.fillna(0, inplace=True)
    
        #Changing Data Types
        self.df.convert_dtypes()

    def get_beach_data(self, beach_name):
        beach_data = self.df[self.df['beach_name'].str.lower() == beach_name.lower()]
        
        if not beach_data.empty:
            return beach_data.to_dict(orient='records')[0]
        else:
            return None
        
if __name__ == '__main__':
    c = Base()
    print(c.return_string())
    print(c.df)
    c.df.to_csv('beach_clean.csv')