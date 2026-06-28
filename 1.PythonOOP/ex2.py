import math
class TextDataset:
    def __init__(self, text_list):
        self._texts = text_list
    
    def __len__(self):
        return len(self._texts)
    
    def __getitem__(self, index):
        return self._texts[index]
    
    def clean_text(self):
        new_texts = self.lower().strip()
        return new_texts

my_text = TextDataset('   Bravo Leo Messi    ') 
print(my_text.__len__())
print(my_text.__getitem__(4))
print(my_text.clean_text())

