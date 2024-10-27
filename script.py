def get_weather_recommendation(temp, condition):
    # Рекомендации по одежде в зависимости от температуры
    if temp <= 0:
        clothing = "Теплая куртка, шапка, шарф и перчатки"
    elif 0 < temp <= 10:
        clothing = "Куртка и свитер"
    elif 10 < temp <= 20:
        clothing = "Легкая куртка или толстовка"
    elif 20 < temp <= 30:
        clothing = "Футболка и легкие брюки или шорты"
    else:
        clothing = "Легкая одежда, например, футболка и шорты"

    # Дополнительные рекомендации в зависимости от погодных условий
    if condition.lower() in ["дождь", "ливень"]:
        clothing += ", возьми зонт и непромокаемую куртку"
    elif condition.lower() == "снег":
        clothing += ", надень зимние ботинки и теплую шапку"
    elif condition.lower() == "туман":
        clothing += ", будь осторожен на дороге"
    elif condition.lower() == "ветер":
        clothing += ", возьми ветровку"

    return clothing


temperature = float(input("Введите температуру (°C): "))
weather_condition = input("Введите погодные условия (например, дождь, снег, туман, ветер): ")

recommendation = get_weather_recommendation(temperature, weather_condition)
print(f"Рекомендация по одежде: {recommendation}")