import random
from datetime import datetime
from water_electrolits.models import Person

def experiment():
    size=1000000
    slice_size=500
    Person.objects.all().delete() #!
    for _ in range(int(size/slice_size)):
        slice=[]
        for _ in range(slice_size):
            slice.append(
                Person(
                    name=str(random.randint(1,1000)),
                    pe_id=str(
                        random.randint(10**70,10**80)
                    )
                )
            )
        Person.objects.bulk_create(slice, slice_size)

    sum=0
    for _ in range(100):
        start=datetime.now()
        list(Person.objects.filter(
            pe_id=random.randint(
                10**70, 10**80
            )
        ))
        delta = (datetime.now() - start).total_seconds()
        sum = sum+delta
        print('Время выполнения 100 запросов: ' + str(sum) + 'секунд')