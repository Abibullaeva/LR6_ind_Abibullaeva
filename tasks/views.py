# ============================================
# ПОДКЛЮЧЕНИЕ НЕОБХОДИМЫХ БИБЛИОТЕК
# ============================================

from django.shortcuts import render # Для рендеринга HTML-шаблонов
import random # Для генерации случайной нагрузки
import matplotlib # Библиотека для построения графиков
matplotlib.use('Agg') # Использование backend без графического интерфейса (для Replit)
import matplotlib.pyplot as plt  # Основной модуль для построения графиков
import io # Для работы с потоками байтов (сохранение графика в память)
import base64 # Для кодирования графиков в base64 (встраивание в HTML)

# ФУНКЦИЯ ГЕНЕРАЦИИ ГРАФИКОВ В ФОРМАТЕ BASE64
def generate_graphs_base64(hours, hourly_load, buffer_usage, rate_limit, buffer_capacity,
                           days, incoming, blocked, passed, efficiency):
    """Генерация графиков в формате base64"""

    graphs = {} # Словарь для хранения закодированных графиков

    # График 1: Заполнение буфера
    fig1, ax1 = plt.subplots(figsize=(10, 5))
     # Расчёт процента заполнения буфера от его максимальной ёмкости
    buffer_percent = [min(100, (b / buffer_capacity) * 100) for b in buffer_usage]
    # Построение линейного графика
    ax1.plot(hours, buffer_percent, 'b-o', linewidth=2, markersize=4, label='Заполнение буфера')
    ax1.axhline(y=90, color='red', linestyle='--', linewidth=2, label='Порог алерта (90%)')
    ax1.axhline(y=50, color='orange', linestyle='--', linewidth=1.5, label='Внимание (50%)')
    # Подписи осей и заголовок
    ax1.set_xlabel('Время (часы)')
    ax1.set_ylabel('Заполнение буфера (%)')
    ax1.set_title('Динамика заполнения буфера')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Сохранение графика в поток байтов (без сохранения на диск)
    buf1 = io.BytesIO()
    fig1.savefig(buf1, format='png', dpi=100, bbox_inches='tight')
    buf1.seek(0) # Перемещение указателя в начало потока
    graphs['buffer'] = base64.b64encode(buf1.getvalue()).decode('utf-8') # Кодирование в base64
    plt.close(fig1) # Закрытие фигуры для освобождения памяти

    # График 2: Скорость потока
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    colors = ['red' if l > rate_limit else 'green' for l in hourly_load]
    # Построение столбчатой диаграммы
    ax2.bar(hours, hourly_load, color=colors, alpha=0.7, label='Входящий поток')
    # Линия порога скорости
    ax2.axhline(y=rate_limit, color='blue', linestyle='--', linewidth=2, label=f'Порог ({rate_limit} зап/сек)')
    ax2.set_xlabel('Время (часы)')
    ax2.set_ylabel('Скорость потока (записей/сек)')
    ax2.set_title('Мониторинг скорости потока данных')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png', dpi=100, bbox_inches='tight')
    buf2.seek(0)
    graphs['flow_rate'] = base64.b64encode(buf2.getvalue()).decode('utf-8')
    plt.close(fig2)

    # График 3: Эффективность фильтрации
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    # Расчёт количества записей, ушедших напрямую и в буфер
    direct_write = [min(x, rate_limit) for x in incoming] # В пределах порога
    buffered = [max(0, x - rate_limit) for x in incoming] # Превышение
    x_pos = list(range(len(days)))
    width = 0.35
    # Два набора столбцов: прямая запись (зелёный) и буфер (оранжевый)
    ax3.bar([p - width/2 for p in x_pos], direct_write, width, label='Прямая запись', color='green', alpha=0.7)
    ax3.bar([p + width/2 for p in x_pos], buffered, width, label='В буфер', color='orange', alpha=0.7)
      # Подписи процентов эффективности над столбцами
    for i, eff in enumerate(efficiency):
        ax3.text(i, incoming[i] + 20, f'{eff:.1f}%', ha='center', fontsize=8, fontweight='bold')
    ax3.set_xlabel('День недели')
    ax3.set_ylabel('Количество записей')
    ax3.set_title('Эффективность фильтрации по дням недели')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(days)
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')

    buf3 = io.BytesIO()
    fig3.savefig(buf3, format='png', dpi=100, bbox_inches='tight')
    buf3.seek(0)
    graphs['efficiency'] = base64.b64encode(buf3.getvalue()).decode('utf-8')
    plt.close(fig3)

    # График 4: Круговая диаграмма распределения
    fig4, ax4 = plt.subplots(figsize=(8, 8))
    total_incoming = sum(incoming) # Всего записей за неделю
    total_direct = sum(direct_write) # Прямая запись
    total_buffered = sum(buffered) # Ушло в буфер
    labels = ['Прямая запись', 'Буферизовано', 'Потеряно (авария)']
    sizes = [total_direct, total_buffered, total_incoming * 0.01] # 1% потерь при аварии
    colors = ['#4CAF50', '#FF9800', '#F44336']
    explode = (0.05, 0.1, 0.15) # Выделение секторов

    # Построение круговой диаграммы
    ax4.pie(sizes, labels=labels, colors=colors, explode=explode,
            autopct='%1.1f%%', shadow=True, startangle=90,
            wedgeprops={'lw': 1, 'ls': '-', 'edgecolor': 'k'})
    ax4.set_title('Распределение обработки запросов\n(Контейнер безопасности)', fontsize=13, fontweight='bold')

    buf4 = io.BytesIO()
    fig4.savefig(buf4, format='png', dpi=100, bbox_inches='tight')
    buf4.seek(0)
    graphs['distribution'] = base64.b64encode(buf4.getvalue()).decode('utf-8')
    plt.close(fig4)

    return graphs # Возвращаем словарь с четырьмя графиками


# ГЛАВНАЯ ФУНКЦИЯ (VIEW) ДЛЯ ОБРАБОТКИ ЗАПРОСОВ
def index(request):
    """Главная страница"""

    # Значения по умолчанию
    abonents = int(request.GET.get('abonents', 16000))
    calls_per_day = int(request.GET.get('calls_per_day', 4))
    sms_per_day = int(request.GET.get('sms_per_day', 2))
    critical_free_percent = int(request.GET.get('critical_free_percent', 10))
    rate_limit_per_sec = int(request.GET.get('rate_limit_per_sec', 2000))
    buffer_capacity = int(request.GET.get('buffer_capacity', 10000))

     # 2. РАСЧЁТ ОБЩЕЙ НАГРУЗКИ
    total_records_per_day = abonents * (calls_per_day + sms_per_day)

    # Почасовая нагрузка
    hours = list(range(1, 25)) # Часы от 1 до 24
    random.seed(42) # Фиксация seed для воспроизводимости
    hourly_load = [1200 + random.randint(-200, 800) for _ in hours] # Базовая нагрузка
    for i in range(8, 20): # Пиковые часы (9:00 – 20:00)
        hourly_load[i] += 500

    # 4. РАСЧЁТ ЗАПОЛНЕНИЯ БУФЕРА
    buffer_usage = []
    for load in hourly_load:
        
        overflow = max(0, load - rate_limit_per_sec) # Превышение порога
        buffer_usage.append(overflow * 3600) # Записей в буфер за час (сек * 3600)

    # Эффективность по дням недели
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    incoming = [1850, 1920, 2100, 2050, 2200, 1300, 1100] # Входящая нагрузка по дням
    blocked = [max(0, x - rate_limit_per_sec) for x in incoming] # Заблокировано
    passed = [min(x, rate_limit_per_sec) for x in incoming]   # Пропущено
    efficiency = [round(b/i*100, 1) if i > 0 else 0 for b, i in zip(blocked, incoming)]

    # Финансовые расчёты
    cost_per_day = 500000 # Стоимость простоя хранилища в день (по ТЗ)
    payback_months = round((800000 / (cost_per_day * 30)) * 12, 1)# Окупаемость в месяцах

    # Графики
    graphs = generate_graphs_base64(
        hours, hourly_load, buffer_usage, rate_limit_per_sec,
        buffer_capacity, days, incoming, blocked, passed, efficiency
    )
    # ФОРМИРОВАНИЕ КОНТЕКСТА ДЛЯ ПЕРЕДАЧИ В ШАБЛОН
    context = {
        'current_params': {
            'abonents': abonents,
            'calls_per_day': calls_per_day,
            'sms_per_day': sms_per_day,
            'critical_free_percent': critical_free_percent,
            'rate_limit_per_sec': rate_limit_per_sec,
            'buffer_capacity': buffer_capacity,
        },
        'total_records_per_day': total_records_per_day,
        'payback_months': payback_months,
        'graphs': graphs, # Словарь с четырьмя графиками в base64
    }
     #  РЕНДЕРИНГ HTML-СТРАНИЦЫ с передачей контекста
    return render(request, 'index.html', context)