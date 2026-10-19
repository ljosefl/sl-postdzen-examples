# Рассчитывает стоимость одного полезного ответа от ИИ-агента, учитывая разработку, поддержку и обучение.

# Стоимость миллиона токенов
TOKEN_COST = 1_000_000

# Стоимость разработки ИИ-агентов (50% от стоимости миллиона токенов)
DEVELOPMENT_COST = TOKEN_COST * 0.5

# Стоимость поддержки и обучения (20% от стоимости миллиона токенов)
SUPPORT_AND_TRAINING_COST = TOKEN_COST * 0.2

# Общие затраты на разработку, поддержку и обучение
TOTAL_COST = DEVELOPMENT_COST + SUPPORT_AND_TRAINING_COST

# Количество тикетов, решаемых за миллион токенов
TICKETS_PER_MILLION_TOKENS = 100

# Стоимость одного тикета без учета дополнительных затрат
TOKEN_COST_PER_TICKET = TOKEN_COST / TICKETS_PER_MILLION_TOKENS

# Количество тикетов, решаемых за один токен
TICKETS_PER_TOKEN = 60 / 2  # 60 минут / 2 минуты на тикет

# Стоимость одного полезного ответа с учетом всех затрат
TOTAL_TOKEN_COST_PER_TICKET = (TOTAL_COST / TICKETS_PER_MILLION_TOKENS) + (TOKEN_COST_PER_TICKET / TICKETS_PER_TOKEN)

print(f"Стоимость одного полезного ответа: {TOTAL_TOKEN_COST_PER_TICKET:.2f} токенов")