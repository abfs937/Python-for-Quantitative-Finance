import pandas as pd

class Parties(object):

    def __init__(self):
        self.df = pd.read_csv('parties.csv')

    def get_lei_from_legal_entity(self):
        self.LEGAL_ENTITY_NAME = input('Please enter the LEGAL_ENTITY_NAME you want to search: ')
        self.LEI_Result = self.df[self.df['LEGAL_ENTITY_NAME'] == self.LEGAL_ENTITY_NAME]['LEI'].values
        print(self.LEI_Result)

    def get_legal_entiry_name_from_lei(self):
        self.LEI = input('Please enter the LEI you want to search: ')
        self.LEGAL_ENTITY_NAME_Result = self.df[self.df['LEI'] == self.LEI]['LEGAL_ENTITY_NAME'].values
        print(self.LEGAL_ENTITY_NAME_Result)


if __name__ == '__main__':
    call_class = Parties()
    call_class.get_lei_from_legal_entity()
    call_class.get_legal_entiry_name_from_lei()
