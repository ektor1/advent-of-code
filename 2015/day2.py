with open("input-day2.txt", "r") as file:
    gift_dimensions = file.read().split("\n")[:-1]

    
gift_dimensions = [gift.split('x') for gift in gift_dimensions]
gift_dimensions = [list(map(int, gift)) for gift in gift_dimensions]

def wrapping_paper_calculator(gift_dimensions):

    paper = 0
    for gift in gift_dimensions:
        l, w, h = gift 
        smallest_side = min(l * w, l * h, w * h)
        paper += 2*l*w + 2*w*h + 2*h*l + smallest_side
    
    return paper

def ribbon_calculator(gift_dimensions):

    ribbon = 0
    for gift in gift_dimensions:
        gift.sort()
        cubic_feet = 1
        
        for d in gift:
            cubic_feet *= d

        ribbon += 2 * gift[0] + 2 * gift[1] + cubic_feet 

    return ribbon

