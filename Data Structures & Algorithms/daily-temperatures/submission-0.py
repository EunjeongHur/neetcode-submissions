# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         res = []

#         # def helper(n, temperature):
#         #     for temp in temperature:
#         #         if temp > stack[]:
#         #             res.append(len(stack))
#         #             return 
#         #         elif temp < stack[]:
#         #             helper(n+1, temperature[n+1:])
#         def helper(n, temperature):
#             if not temperature:
#                 res.append(0)
#                 return
#             for temp in temperature:
#                 if not stack:
#                     stack.append(temp)
#                     helper(n+1, temperature[n+1:])
#                     stack.pop()
#                 elif temp > stack[0]:
#                     res.append(len(stack))
#                     break
#                     return
#                 elif temp <= stack[0]:
#                     stack.append(temp)
#                     helper(n+1, temperature[n+1:])
#                     stack.pop()

#                 n +=1 

#         helper(0, temperatures)

#         # for temperature in temperatures:
#             # if not stack:
#             #     stack.append(int(temperature))
#             # elif temperature >= stack[-1]:
#             #     stack.append(int(temperature))
#             # elif temperature < stack[-1]:
#             #     res.append(len(stack)-1)
#             #     stack = []
#             # print(stack)
#             # print(res)


#         return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # 결과 리스트 미리 크기만큼 초기화
        stack = []  # 스택에는 인덱스를 저장

        def helper(n):
            if n >= len(temperatures):
                return
            
            # 현재 온도보다 높은 온도가 나올 때까지 스택에서 처리
            while stack and temperatures[n] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = n - index  # 며칠 뒤에 더 따뜻해지는지 계산

            stack.append(n)  # 현재 온도를 스택에 추가
            helper(n + 1)  # 재귀적으로 다음 온도를 처리

        helper(0)
        return res
