from django.test import TestCase



def test_get_WebtoonDetailSerializer_ok():
  some_data = {} # 의도한 데이터 
  input1, input2 = "", ""
  serializer = _get_WebtoonDetailSerializer(input1, input2)
  
  assert serialzer.data == some_data
  
  
