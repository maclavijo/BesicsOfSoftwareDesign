from abc import ABC, abstractmethod

#Obeserver / Subscriber class

class Observer(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError
    
class User(Observer):
    def __init__(self,username):
        self.username = username
        self.movielist = []
        
    def update(self,title):
        print('---------------------------------------')
        print('Users are being notified of new movies:')
        print('User ' + self.username + ' has been updated!!')
        state = title.get_state()
        if state not in self.movielist:
            self.movielist.append(state)
        
    def watchMovie(self):
        print(f'{self.username} is watching {self.movielist}')

# Observable class
class MovieList:
    def __init__(self):
        self.movielist = []
        self._observersList = []

    def addMovie(self,movie):
        self.movielist.append(movie)
        self._notify()

    def _notify(self):
        for observer in self._observersList:
            observer.update(self)

    def get_state(self):
        return self.movielist

    def addUser(self,observer):
        self._observersList.append(observer)

#Creates Drama and Action Movie classes
class Drama(MovieList):
    pass
class Action(MovieList):
    pass

def main():

    print('Observer Design Pattern Example')

    #Creating users and movie categories
    peter = User('Peter')
    DramaMovies = Drama()
    ActionMovies = Action()

    DramaMovies.addUser(peter)
    ActionMovies.addUser(peter)

    DramaMovies.addMovie('Parasite')
    ActionMovies.addMovie('Fast and Furious')

    print('')
    print('############################')
    print('What are users watching now?')
    print('############################')
    peter.watchMovie()
    print('')

    ActionMovies.addMovie('Avengers')
    ActionMovies.addMovie('Justice League')

    print('')
    print('############################')
    print('What are users watching now?')
    print('############################')
    peter.watchMovie()
    print('')

if __name__ == '__main__':
    main()
