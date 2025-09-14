print("tugas mini prjoect DDP")
print("Farrel Fazzadinata Sumarna")

nama_team1 = str(input("masukkan nama tim kebanggan loh : "))
nama_team2 = str(input("masukkan nama tim kebanggan loh : "))

junggle_team1 = int(input("berapa junggle yang didapat : "))
junggle_team2 = int(input("berapa junggle yang didapat : "))
turret_team1 = int(input("berapa turret yang didapat : "))
turret_team2 = int(input("berapa turret yang didapat : "))
kill_team1 = int(input("berapa kill yang didapat : "))
kill_team2 = int(input("berapa kill yang didapat : "))

score_team1 = (junggle_team1*2) + (turret_team1*3) + (kill_team1*100)
score_team2 = (junggle_team2*2) + (turret_team2*3) + (kill_team2*100)

if score_team1 >= score_team2 :
    print( "weh keren " + nama_team1 + " menang dengan " + str(score_team1) + " point dari " + nama_team2 + " dengan point " + str(score_team2))
else :
    print( "weh keren " + nama_team2 + " menang dengan " + str(score_team2) + " point dari " + nama_team1 + " dengan point " + str(score_team1))


