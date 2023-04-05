rating = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: {rating}")

new_scores_count = int(input("Кол-во новых элементов: "))

for i in range(1, new_scores_count + 1):
    new_score = int(input("Введите новый элемент: "))
    if new_score > 0:
        rating.append(new_score)
        rating.sort(reverse=True)
        print(f"Новый рейтинг: {rating}")
