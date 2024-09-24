# Pythonでは優先度付きキューがライブラリとして実装されている
import heapq
scores = [12, 46, 33, 27, 73, 88, 55, 45, 68, 63, 77, 15, 99]
print(heapq.nlargest(3, scores)) # 高得点上位３組を出力
print(heapq.nsmallest(5, scores)) # 得点が低い下位5組を出力
print(scores) # 元のリストはそのまま

# heappopはリストの最小値を取り出す
print(heapq.heappop(scores)) # 12
print(scores) # 元のリストから12が取り出されたので要素数が減っている
