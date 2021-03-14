def likelihood():
    likelihoods = (50, 38, 27, 99, 4 )
    return likelihoods

def run():
    minvalue = min(likelihood())
    maxvalue = max(likelihood())
    print(f"the minimum likelihood of falling : {minvalue}% \nthe maximum likelihood of falling : {maxvalue}%")
    
if __name__ == '__main__':
    run()