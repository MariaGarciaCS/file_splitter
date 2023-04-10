import csv

def string_to_csv(input, filename):
    
    values = input.split()

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        next_precinct = ""

        while(len(values) >= 13):
            if(next_precinct):
                current_row = [next_precinct] + values[:12]
                last_val = values[12][:-4]
                next_precinct = values[12][-4:]
                values = values[13:]
            else:
                #for first iteration
                current_row = values[:13]
                last_val = values[13][:-4]
                next_precinct = values[13][-4:]
                values = values[14:]
                current_row = current_row + [last_val]
            
            print("next precinct: ", next_precinct)
            print("last_value: ", last_val)
            print(current_row)

            current_row.append(last_val)



       



        # for i in range(0, len(values)):
        #     current_row = values[:13]
        #     if i % 14 == 13:
        #         last_four_chars = values[i][-4:]
        #         first_part = values[i][:-4]

        #         print("precinct: ", last_four_chars)
        #         print("last_value: ", first_part)

               
        #         current_row.append(first_part)
        #         csvwriter.writerow(current_row)

              
        #         csvwriter.writerow([last_four_chars])

        #         current_row = []
        #     else:
        #         current_row.append(values[i])

        # if current_row:
        #     csvwriter.writerow(current_row)

    print("\n --- success ---")


input = "0004 252 563 815 1,794 45.43% 336 55 84 22 18 52 61 120005 181 498 679 1,494 45.45% 206 73 78 19 14 55 72 70043 226 184 410 2,036 20.14% 39 14 105 37 10 39 52 60044 143 278 421 2,173 19.37% 63 39 38 8 8 77 14 100046 210 211 421 2,648 15.90% 54 47 29 6 9 116 17 110053 412 710 1,122 3,313 33.87% 414 60 154 35 19 60 96 160054 254 325 579 1,728 33.51% 98 39 109 19 18 35 66 80055 225 411 636 3,157 20.15% 101 55 79 33 22 51 68 150057 557 794 1,351 3,469 38.94% 475 81 156 47 11 52 123 160058 412 640 1,052 3,570 29.47% 186 62 164 44 27 65 99 100059 443 663 1,106 2,966 37.29% 339 102 165 58 12 64 107 180075 228 374 602 2,047 29.41% 142 54 92 17 6 36 62 70078 155 168 323 1,727 18.70% 29 31 40 12 10 80 26 90086 425 660 1,085 4,163 26.06% 182 68 160 64 55 89 109 190105 128 175 303 2,458 12.33% 36 8 36 9 7 96 21 120117 127 157 284 1,986 14.30% 21 15 54 12 17 37 48 140153 86 161 247 2,059 12.00% 19 20 32 9 8 71 18 90166 114 280 394 1,349 29.21% 79 54 51 19 16 45 27 120167 1 0 1 18 5.56% 0 0 0 0 0 1 0 00179 187 230 417 2,000 20.85% 29 23 95 22 10 48 75 90184 57 116 173 1,136 15.23% 21 11 18 5 7 36 11 30206 275 525 800 3,284 24.36% 153 67 97 20 18 123 64 150207 179 284 463 1,218 38.01% 66 71 51 11 17 85 34 80270 579 615 1,194 3,997 29.87% 111 118 271 53 154 78 169 140299 134 144 278 1,655 16.80% 27 14 40 18 15 40 36 60313 3 8 11 75 14.67% 1 1 0 1 1 0 3 00323 167 258 425 1,940 21.91% 67 22 65 34 17 53 50 50330 237 295 532 2,493 21.34% 64 16 131 31 20 62 79 140339 184 226 410 2,134 19.21% 25 36 30 7 16 103 18 80341 42 109 151 1,434 10.53% 17 4 27 5 5 40 8 80446 25 18 43 343 12.54% 5 2 4 1 1 11 5 00501 258 489 747 2,290 32.62% 211 47 77 29 17 56 65 90505 442 645 1,087 4,187 25.96% 167 62 194 61 85 106 117 15"

string_to_csv(input, "output.csv")