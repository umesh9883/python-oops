class Author:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname

    def __str__(self) -> str:
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self,name,pagecount) -> None:
        self.name=name
        self.pagecount=pagecount



class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author=author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getPageCount(self):
        result=0
        for chapter in self.chapters:
            result+=chapter.pagecount
        return result

auth=Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)
ch1=Chapter("Chapter 1", 125)
ch2=Chapter("Chapter 2", 97)
ch3=Chapter("Chapter 3", 143)

b1.addchapter(ch1)
b1.addchapter(ch2)
b1.addchapter(ch3)



print(b1.title)
print(b1.author)
print(b1.getPageCount())