select animal_id, name, if (sex_upon_intake like 'int%',  'X', 'O') as 중성화
from animal_ins
order by animal_id