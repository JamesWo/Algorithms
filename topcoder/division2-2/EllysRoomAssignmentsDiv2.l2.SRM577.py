"""
# [EllysRoomAssignmentsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15497&pm=12521)
*Single Round Match 577 Round 1 - Division II, Level Two*

## Statement
Elly is going to take part in a programming contest. Before the contest, each contestant is assigned a room (just like in this SRM).

The contest uses the following room assignment algorithm:
Let the number of registrants be N.
The number of rooms is set to be R = N / 20, if N is divisible by 20, or R = N / 20 + 1 otherwise. Here the '/' operator represents integer division, i.e., the remainder is being ignored.
The registrants are sorted by rating in decreasing order.
The first R registrants are randomly assigned to rooms such that no two of them are in the same room. Then the same is done with the next R registrants and so on, until there are no more unassigned registrants. Note that it is possible for the last group to have less than R registrants, but they are still randomly assigned into rooms in such a way that no two of them are in the same room.

You are given a String[] *ratings*. Concatenate its elements to obtain one long string. It will represent a space-separated list of the contestants' ratings. For simplicity, no two ratings in the list will be equal. Elly's rating is the first one in the list.

Return the probability that she will be assigned to the room to which the person with the highest rating is assigned.

## Definitions
- *Class*: `EllysRoomAssignmentsDiv2`
- *Method*: `getProbability`
- *Parameters*: `String[]`
- *Returns*: `double`
- *Method signature*: `double getProbability(String[] ratings)`

## Constraints
- *ratings* will contain between 1 and 50 elements, inclusive.
- Each element of *ratings* will contain between 1 and 50 characters, inclusive.
- Each character in *ratings* will be either a digit ('0'-'9') or a space (' ').
- Each number in the concatenation of *ratings* will be an integer without leading zeroes.
- Each number in the concatenation of *ratings* will be a unique integer between 1 and 1199, inclusive.
- Every two numbers in the concatenation of *ratings* will be separated by a single space.
- The count of numbers in the concatenation of *ratings* will be between 8 and 652, inclusive.

## Examples
### Example 1
#### Input
<c>["724 42 13 17 1199 577 1001 1101 483 845 196 1163 3", "60 985 296 1044 917 1007 898 119 1016 23 56 1159 1",<br /> "194 372 951 991 947 1053 433 1017 1011 391 110 9 2", "30 245 788 830 747 2 3"]</c>
#### Output
<c>0.3333333333333333</c>
#### Reason
There are 43 registrants, one of them is Elly. Her raiting is 724. The contestants will be distributed into (43/20) + 1 = 3 rooms. One of the rooms will have 15 contestants and each of the other two will have 14.

### Example 2
#### Input
<c>["42 911 666 17 13 1 1155 1094 815 5 1000 540"]</c>
#### Output
<c>1.0</c>
#### Reason
With only 12 people competing, they will all be in the same room.

### Example 3
#### Input
<c>["1168 196 440 643 227 1194 1149 372 878 23 767 296 ", "110 52 840 367 790 884 620 676 380 1007 304 262 10",<br /> "63 917 230 951 635 898 894 319 724 597 470 1143 62", "7 1175 436 484 457 991 433 747 8 94 830 1044 1053 ",<br /> "360 1167 391 364 1120 192 56 528 366 712 480 83 11", "59 483 949 356 1163 9 845 750 781 784 1016 985 346",<br /> " 466 947 73 911 690 630 609 866 788 98 1017 410 11", "9 617 245 801 205"]</c>
#### Output
<c>0.0</c>
#### Reason
There are five rooms in this case. Being the third highest rated, the room assignment algorithm will never put her in the same room with the person with the highest rating.

### Example 4
#### Input
<c>["470 840 410 1168 637 464 498 1118 276 1013 989 874", " 64 192 296 611 44 999 583 365 1195 20 838 274 425",<br /> " 236 960 1116 857 630 664 98 1046 807 1111 529 47 ", "31 676 1112 42 376 56 1105 814 6 871 364 319 1145 ",<br /> "491 199 1121 713 353 956 579 445 1031 627 618 202 ", "763 271 188 1140 1044 311 895 1175 74 465 454 708 ",<br /> "1181 866 387 99 784 700 308 853 977 253 62 782 371", " 8 908 1151 83 932 55 1077 897 517 767 990 567 869",<br /> " 607 603 499 356 772 310 332 357 845 1159 1128 104", "2 783 953 315 1020 360 696 793 847 1 716 731 1097 ",<br /> "660 302 761 484 23 89 609 161 978 312 87 363 879 6", "02 635 409 749 475 106 632 961 1053 414 422 1146 6",<br /> "51 970 907 719 110 118 218 471 334 747 645 575 757", " 156 137 101 150 1084 48 859 1016 396 779 791 195 ",<br /> "1148 138 141 304 523 1129 940 569 1058 113 949 967", " 261 1017 433 126 205 679 998 325 831 239 774 245 ",<br /> "992 407 991 667 489 580 628 1055 383 924 706 369 8", "37 380 596 392 734 183 397 1165 911 657 1028 617 1",<br /> "45 105 870 707 447 281 841 526 367 297 66 851 643 ", "1142 168 480 3 347 1101 737 1025 647 588 1049 458 ",<br /> "508 759 654 927 744 937 402 440 1158 620 1067 528 ", "1001 1186 705 124 511 597 395 1063 399 753 1093 10",<br /> "05 717 1173 278 81 762 71 51 801 890 1185 413 674 ", "252 805 775 52 612 1075 1187 131 559 72 1141 298 8",<br /> "5 640 1184 290 1127 423 925 1108 114 864 605 802 1", "39 962 104 817 289 816 359 323 1068 368 477 1022 2",<br /> " 377 512 688 1029 340 28 1193 910 417 984 1163 385", " 858 212 119 898 9 473 180 140 346 262 971 170 564",<br /> " 226 123 698 196 10 466 1174 446 248 1194 227 94 3", "09 850 1179 1035 680 750 67 650 765 61 982 412 736",<br /> " 149 822 933 621 117 1062 678 929 693 125 836 852 ", "694 711 275 358 524 825 997 372 781 873 725 818 57",<br /> "1 1041 460 796 287 723 142 322 691 220 830 778 116", "7 68 1059 1011 958 324 200 947 29 216 57 443 488 9",<br /> "85 666 690 1182 230 1114 153 73 1086 191 1010 586 ", "250 96 211 40 217 1155 82 641 1066 1131 896 154 22",<br /> "4 5 951 917 1189 709 777 1034 724 436 626 270 1052", " 593 50 926 901 634 1082 943 894 721 945 366 391 4",<br /> "27 646 1076 712 496 868 435 1120 177 1149 330 483 ", "1152 351 176 457 1126 235 1143 790 780 1166 686 80",<br /> " 121 222 305 355 581 476 34 533 147 316 881 539 45", " 146 263 22 788 527 519 1069 710 59 148 234 661 81",<br /> "3 1081 133 884 548 405 344 451 887 789 1007 295 39", "8 728 553 642 878 77 293 684 877 554 478"]</c>
#### Output
<c>0.037037037037037035</c>
#### Reason
In this case the number of competitors is 540, which is divisible by 20. Thus, the number of rooms is 27.


"""
def getProbability(ratings):
    ratings = "".join( ratings)
    ratings = map(int, ratings.split( " " ))
    scores = []
    for num in ratings:
        if num not in scores:
            scores.append(num)
    elly = scores[0]
    scores.sort(reverse=True)
    if elly == scores[0]:
        return 1
    numRooms = (len(scores)+19) / 20
    if elly in scores[0:numRooms]:
        return 0
    return float(1) / numRooms

