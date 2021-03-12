filename = 'exported_bots.csv'


def export(filename, num_bots):
    print('Exporting...') 
    with open(filename, "a") as file:
        
        print('please enter the number of bots you want to export')

       

        for _ in range(num_bots):

            bot_id = int(input('Please enter bot ID'))
            bot_name = input('Please enter bot name')
            bot_paint = input('Please enter bot paint')
    
            file.write(f"{bot_id}',{bot_name},{bot_paint} \n")
        

    print("Done")

   

def run():
    export(filename, 2)
    
if __name__ == '__main__':
    run()