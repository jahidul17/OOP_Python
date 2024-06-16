class Star_Cinema:
    hall_list=[]
    
    def entry_hall(self,hall_obj):
        self.hall_list.append(hall_obj)

class Hall(Star_Cinema):
    def __init__(self,rows ,cols ,hall_no ) -> None:
        self.__seats={}
        self.__show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        
        
    def entry_show(self,id, movie_name, time):
        show=(id,movie_name,time)
        self.__show_list.append(show)
        self.__seats[id]=[]
        for i in range(self.rows):
            col=[]
            for j in range(self.cols):
                col.append(0)
            self.__seats[id].append(col)
        

    def book_seats(self,id,row,col):
        if id in self.__seats:
            if 0<=row and row<self.rows and 0<=col and  col< self.cols:
                if self.__seats[id][row][col]==0:
                    self.__seats[id][row][col]=1
                    print(f'Congratulation! Your seat [{row} {col}] Booked.')
                else:
                    print(f'Sorry! This seat is not available.')                     
            else:
                print(f'Invalid Seat.')
        else:
            print(f'Sorry! Your Id "{id}" is not valid.')
        print("\n     ------------------------------      \n")
            
    def view_show_list(self):
        for show in self.__show_list:
            (movieid,moviename,time)=show 
            print(f"Movie Title:{moviename} Show Id: {movieid} Showing Time: {time}")
        print("\n     ------------------------------      \n")
      
      
    def view_available_seats(self,id):
        if id in self.__seats:
            print("Avalible seats are: ")
            for row in range(self.rows):
                for col in range(self.cols):
                    print(f'-[{self.__seats[id][row][col]}]-',end=" ")
                print('\n')
            print("Here, 0 means empty and 1 means fill up")
        else:
            print('ID {id} is not found.')
        print("\n     ------------------------------      \n")  
         
        
hall_one=Hall(7, 8, 1)

hall_one.entry_show(10,"Spider Man","10.00 am")
hall_one.entry_show(20,"Iron Man","12.00 pm")
hall_one.entry_show(30,"Super Man","03.00 pm")
hall_one.entry_show(40,"Avater","06.00 pm")

while True:
    print(f'Select Option form below:')
    print(f'1: View all show today')
    print(f'2: View available seats')
    print(f'3: Book Tricket')
    print(f'4: Exit')
    
    op= int(input("Enter Option: "))
    if op==1:
        hall_one.view_show_list()
        
    elif op==2:
        print(f'Please Insert id: ')
        id=int(input())
        hall_one.view_available_seats(id)
        
    elif op==3:
        print(f'Please insert id , seat row and seat column')
        id=int(input())
        s_row=int(input())
        s_col=int(input())
        hall_one.book_seats(id,s_row,s_col)
        
    elif op==4:
        break
    else:
        break
    