# class Solution:
#     def twoSum(self, nums, target: int) :
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]

#         return []

# salom=Solution()
# d=salom.twoSum([2,7,11,15],9)
# print(d)

# Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int):
#         if x>=0:
#             return x==int(str(x)[::-1])
#         return False


# salom = Solution()
# d=salom.isPalindrome(120)
# print(d)

# Roman to Integer

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         value = 0
#         last_digit_value = 0
        
#         for roman_digit in num[::-1]:            
#             digit_value = value_map[roman_digit]

#             if digit_value >= last_digit_value:       
#                 value += digit_value         
#                 last_digit_value = digit_value
#             else:                                     
#                 value -= digit_value

#         return value
        

import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

data = {
    'dbname': 'servis',
    'user': 'servis',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5432
}

conn = None  

try:
    conn = psycopg2.connect(**data)  
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS universitetlar (
        id SERIAL PRIMARY KEY,
        nomi VARCHAR(200) NOT NULL,
        manzili TEXT,
        asos_sanasi DATE
    )
    """)
    
    cursor.executemany("""
    INSERT INTO universitetlar (nomi, manzili, asos_sanasi)
    VALUES (%s, %s, %s)
    """, [
        ('Toshkent Davlat Universiteti', 'Toshkent shahar, Universitet kochasi', '1918-05-06'),
        ("O'zbekiston Milliy Universiteti", 'Toshkent shahar, Universitet kochasi', '1947-10-12'),
        ('Inha Universiteti', "Toshkent shahar, Ziyolilar ko'chasi", '2014-09-01')
    ])
    
    conn.commit() 

    universitet_nomi = 'Toshkent Davlat Universiteti'
    
    cursor.execute("""
    SELECT * FROM universitetlar WHERE nomi = %s
    """, (universitet_nomi,))
    
    print(f"{universitet_nomi} haqida ma'lumot:")
    for row in cursor.fetchall():
        print(f"Nomi: {row[1]}, Manzili: {row[2]}, Asos sanasi: {row[3]}")
    
except psycopg2.Error as e:
    print(f"Xato yuz berdi: {e}")
    if conn:
        conn.rollback()
finally:
    if conn:
        cursor.close()
        conn.close()
