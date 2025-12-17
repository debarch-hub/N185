# Dict
# 1-vazifa. O’quvchilarning ismi va yoshi dict ko’rinishida berilgan. Yoshi 18 va undan katta o’quvchilarni ekranga chiqaring,
# Input : 
# students = {
# 	"Samandar": 18,
# 	"Muzaffar": 19,
# 	"Xojiakbar": 16,
# 	"Islom": 20,
# 	"Asomiddin": 14,
# 	"Sobitjon": 17,
# 	"Shoxruh": 20
# }

# Output: Samandar, Muzaffar, Islom, Shoxruh

students = {
	"Samandar": 18,
 	"Muzaffar": 19,  
 	"Xojiakbar": 16,
 	"Islom": 20,
 	"Asomiddin": 14,
 	"Sobitjon": 17,
 	"Shoxruh": 20
}
for ism in students:
    if students[ism] >= 18:
        print(ism, end=", ")
