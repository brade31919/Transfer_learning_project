#latlon_file is the .txt file which records the longitude and latitude of the point
#pname_file is the .txt file which records the pano name of the newest pano
#old_pname_file is the .txt file which records the pano name of the old pano
def Dl(latlon_file,pname_file,old_pname_file):
    f = open(latlon_file,'r')
    i =0
    #if crash change this start point to the crash point
    star_point = 349
    a = open("/home/Horatio/svdata/record.txt",'w')
    for line in f:
        print line
        if(i>= star_point):
            try:
                latlon = line   #read in the (lon,lat) information
                Findlatlon(latlon,pname_file,old_pname_file,i)
                a.write("The %d-th pair of latlon has completed without error!\n"%i)
            except:
                a.write("Error occur at %d-th pair\n"%i)
        i = i+1
    a.close()
    f.close()
def Findlatlon(latlon,pname_file,old_pname_file,i):
    #25.0378019,121.5581245
    click("1453812687994.png")
    #if the map is open, no need to open a new page
    if exists("1453816570455.png") or exists("1453816597960.png"):
        click("1453821129934.png")
        #if the google map is in search page
        if exists("1453813492579.png"):
            click("1453812910298.png")
            wait(2)
            type(latlon)
            type(Key.ENTER)
            wait(6)
            dragDrop("1455534980223.png", Location(1197,540))
            wait(4)
            '''
            click("1453816695712.png")
            type('a',KeyModifier.CTRL)
            type('c',KeyModifier.CTRL)
            click("1453818326187.png")
            wait(2)
            type("gedit "+pname_file+str(i)+"-0" + ".txt")
            type(Key.ENTER)
            wait(2)
            type('v',KeyModifier.CTRL)
            click("1453818263426.png")
            click("1453818326187.png")
            wait(1)
            type('c',KeyModifier.CTRL)
            '''
            j=0
            while(j<8):
                click("1453819815668.png")
                if j==0:
                    click("1453819848829.png")
                    wait(1)
                    Region(137,341,267,67).click("1455688655225.png")
                else:
                    Region(137,341,267,67).click("1455688655225.png")
                    type(Key.RIGHT)
                wait(2)
                click(Location(300,300))
                wait(2)
                click("1453816695712.png")
                type('a',KeyModifier.CTRL)
                type('c',KeyModifier.CTRL)
                click("1453818326187.png")
                wait(2)
                type("gedit "+old_pname_file+str(i)+"-"+str(j)+".txt")
                type(Key.ENTER)
                wait(3)
                type('v',KeyModifier.CTRL)
                wait(1)
                click("1453818263426.png")
                #click("1453818326187.png")
                wait(2)
                type('q',KeyModifier.CTRL)
                if j>0:
                    f = open(old_pname_file + str(i) + "-" + str(j)+".txt",'r')
                    g = open(old_pname_file + str(i) + "-" + str(j-1)+ ".txt",'r')
                    for line in f:
                        a = line
                    for line in g:
                        b = line
                    print "fku"
                    print a
                    print b
                    if a == b:
                        break
                j=j+1
                wait(2)
                
        #if the map is not in the search page, it would be in the panorama page    
        else: 
            wait(2)
            click(Location(1197,540))
            
            type(Key.ESC)
            #click("1453819076044.png")
           # find("1453814711941.png")
            wait(1)
            click("1453814739493.png")
            click("1453812910298.png")
            wait(2)
            type(latlon)
            type(Key.ENTER)
            wait(6)
            hover("1455534980223.png")
            mouseDown(Button.LEFT)
            wait(0.5)
            mouseMove(Location(1197,525))
            wait(1)
            mouseUp(Button.LEFT)
            #dragDrop("1455534980223.png", Location(1197,525))
            wait(4)
            '''
            click("1453816695712.png")
            type('a',KeyModifier.CTRL)
            type('c',KeyModifier.CTRL)
            click("1453818326187.png")
            wait(2)
            type("gedit "+pname_file+str(i)+".txt")
            type(Key.ENTER)
            wait(2)
            type('v',KeyModifier.CTRL)
            click("1453818263426.png")
            #click("1453818326187.png")
            wait(1)
            type('q',KeyModifier.CTRL)
            '''
            j=0
            while(j<8):
                click("1453819815668.png")
                if j==0:
                    click("1453819848829.png")
                    wait(1)
                    Region(137,341,267,67).click("1455688655225.png")
                else:
                    Region(137,341,267,67).click("1455688655225.png")
                    type(Key.RIGHT)
                wait(2)
                click(Location(300,300))
                wait(2)
                click("1453816695712.png")
                type('a',KeyModifier.CTRL)
                type('c',KeyModifier.CTRL)
                click("1453818326187.png")
                wait(2)
                type("gedit "+old_pname_file+str(i)+"-"+str(j)+".txt")
                type(Key.ENTER)
                wait(3)
                type('v',KeyModifier.CTRL)
                wait(1)
                click("1453818263426.png")
                #click("1453818326187.png")
                wait(2)
                type('q',KeyModifier.CTRL)
                if j>0:
                    f = open(old_pname_file + str(i) + "-" + str(j)+".txt",'r')
                    g = open(old_pname_file + str(i) + "-" + str(j-1)+ ".txt",'r')
                    for line in f:
                        a = line
                    for line in g:
                        b = line
                    print "fku"
                    print a
                    print b
                    if a == b:
                        break
                j=j+1
                wait(2)
    #if the google map is not open, then open a new one
    else:
        find("1453812739531.png")
        
        click("1453957693903.png")
        click("1453814887934.png")
        type("google maps")
        type(Key.ENTER)
        wait(2)
        click("1453815004181.png")
        wait(2)
        click("1453812910298.png")
        wait(2)
        type(latlon)
        type(Key.ENTER)
        wait(6)
        hover("1455534980223.png")
        mouseDown(Button.LEFT)
        wait(0.5)
        mouseMove(Location(1197,525))
        wait(1)
        mouseUp(Button.LEFT)
        #dragDrop("1455534980223.png", Location(1197,525))
        wait(3)
        click("1453816695712.png")
        type('a',KeyModifier.CTRL)
        type('c',KeyModifier.CTRL)
        click("1453818326187.png")
        wait(2)
        type("gedit "+pname_file+str(i)+".txt")
        type(Key.ENTER)
        wait(2)
        type('v',KeyModifier.CTRL)
        click("1453818263426.png")
        click("1453818326187.png")
        wait(1)
        type('c',KeyModifier.CTRL)
        click("1453819815668.png")
        click("1453819848829.png")
        wait(1)
        click("1453820168124.png")
        wait(2)
        click("1453816695712.png")
        type('a',KeyModifier.CTRL)
        type('c',KeyModifier.CTRL)
        click("1453818326187.png")
        wait(2)
        type("gedit "+old_pname_file+str(i)+".txt")
        type(Key.ENTER)
        wait(2)
        type('v',KeyModifier.CTRL)
        click("1453818263426.png")
        click("1453818326187.png")
        wait(1)
        type('c',KeyModifier.CTRL)
        
Dl("/home/Horatio/svdata/latlon.txt","/home/Horatio/svdata/pname","/home/Horatio/svdata/old_pname")
    
