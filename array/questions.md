# Create a structured Markdown file for DSA Array Questions

import pypandoc

content = """

# 📘 DSA - Array Questions (Category Wise)

Structured for Interview Preparation 🚀

---

## 🔹 1. Basic Array Operations (Foundation)

1. Find the largest and smallest element in an array
2. Find the second largest element
3. Check if array is sorted
4. Reverse an array (in-place)
5. Remove duplicates from sorted array
6. Rotate array by K positions (left/right)
7. Move all zeros to end
8. Count frequency of each element

---

## 🔹 2. Two Pointer Technique

1. Two Sum (sorted array version)
2. Remove duplicates (in-place)
3. Move negative numbers to one side
4. Container With Most Water
5. Trapping Rain Water
6. 3 Sum problem
7. Sort 0s, 1s, 2s (Dutch National Flag problem)

---

## 🔹 3. Sliding Window

1. Maximum sum subarray of size K
2. First negative number in every window of size K
3. Longest substring without repeating characters
4. Maximum number of vowels in substring of size K
5. Longest subarray with sum <= K
6. Minimum size subarray sum

---

## 🔹 4. Kadane’s Algorithm Pattern

1. Maximum subarray sum
2. Maximum product subarray
3. Maximum circular subarray sum
4. Print subarray with maximum sum

---

## 🔹 5. Prefix Sum / Hashing Based

1. Subarray with given sum
2. Count subarrays with sum = K
3. Longest subarray with sum = K
4. Find pivot index
5. Range sum queries

---

## 🔹 6. Sorting Based Problems

1. Merge intervals
2. Insert interval
3. Largest number formed from array
4. Check if two arrays are equal
5. Minimum platforms required

---

## 🔹 7. Advanced Array (Interview Level)

1. Next permutation
2. Majority element (Moore’s Voting Algorithm)
3. Find duplicate number (Floyd’s cycle detection)
4. Missing and repeating number
5. Inversion count
6. Maximum gap
7. Subarray sum divisible by K
8. Product of array except self

---

## 🔹 8. Binary Search on Array

1. Search in rotated sorted array
2. Find peak element
3. First and last occurrence
4. Square root using binary search
5. Allocate minimum pages
6. Aggressive cows problem

---

## 🔥 Must Master Patterns

- Two Pointer
- Sliding Window
- Prefix Sum
- Binary Search
- HashMap usage
- In-place array manipulation

---

💪 Tip: Solve category by category. Focus on understanding patterns instead of memorizing solutions.
"""

output_file = "/mnt/data/dsa-array-questions.md"

pypandoc.convert_text(
content,
'md',
format='md',
outputfile=output_file,
extra_args=['--standalone']
)

output_file
