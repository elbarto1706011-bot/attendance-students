# Калькулятор FP и COCOMO II для attendance-students
WEIGHTS = {"EI": (3, 4, 6), "EO": (4, 5, 7), "EQ": (3, 4, 6),
           "ILF": (7, 10, 15), "EIF": (5, 7, 10)}
LEVELS = {"низкая": 0, "средняя": 1, "высокая": 2}

# (тип, количество, сложность)
components = [
    ("EI", 6, "средняя"),
    ("EO", 2, "средняя"),
    ("EQ", 3, "низкая"),
    ("ILF", 4, "низкая"),
    ("EIF", 0, "низкая"),
]
tdi, sloc_per_fp = 30, 40
sf_sum, em, monthly_rate = 18.0, 1.10, 500

ufp = sum(WEIGHTS[k][LEVELS[level]] * count for k, count, level in components)
vaf = 0.65 + 0.01 * tdi
fp = ufp * vaf
ksloc = fp * sloc_per_fp / 1000
e = 0.91 + 0.01 * sf_sum
pm = 2.94 * (ksloc ** e) * em
f = 0.28 + 0.2 * (e - 0.91)
tdev = 3.67 * (pm ** f)
team = pm / tdev
cost = pm * monthly_rate

print("Проект attendance-students")
print(f"UFP={ufp:.2f}; VAF={vaf:.2f}; FP={fp:.2f}")
print(f"Размер={ksloc:.2f} KSLOC")
print(f"Трудоёмкость={pm:.2f} чел.-мес.")
print(f"Срок={tdev:.2f} мес.; команда={team:.2f} чел.")
print(f"Оценочная стоимость=${cost:,.2f}")
print("\\nАнализ чувствительности по EM:")
for em_value in (0.8, 1.0, 1.1, 1.4):
    pm_value = 2.94 * (ksloc ** e) * em_value
    time_value = 3.67 * (pm_value ** f)
    print(f"EM={em_value:.1f}: PM={pm_value:.2f}; TDEV={time_value:.2f} мес.")
