from numpy import genfromtxt
import gzip
import pickle as cPickle

dirg = 'fold/' 

for i in range(1):

  k = i;
  name1 = dirg+'/train'+str(k)+'_x'
  #train_set_x = genfromtxt(name, delimiter=',')
  name2 = dirg+'/train'+str(k)+'_y'
  #train_set_y = genfromtxt(name, delimiter=',')

  #train_set = train_set_x, train_set_y
  train_set= genfromtxt(name1, delimiter=','),  genfromtxt(name2, delimiter=',')
  #del train_set_x
  #del train_set_y

  name1 = dirg+'/test'+str(k)+'_x'
  #test_set_x = genfromtxt(name, delimiter=',')
  name2 = dirg+'/test'+str(k)+'_y'
  #test_set_y = genfromtxt(name, delimiter=',')
  #test_set = test_set_x, test_set_y
  test_set = genfromtxt(name1, delimiter=','), genfromtxt(name2, delimiter=',')
  #del test_set_x
  #del test_set_y

  name1 = dirg+'/val'+str(k)+'_x'
  val_set_x = genfromtxt(name1, delimiter=',')
  name2 = dirg+'/val'+str(k)+'_y'
  val_set_y = genfromtxt(name2, delimiter=',')
  #val_set = val_set_x, val_set_y
  #del val_set_x
  #del val_set_y
  val_set = genfromtxt(name1, delimiter=','), genfromtxt(name2, delimiter=',')
 
  dataset = [train_set, val_set, test_set]
  del train_set
  del val_set
  del test_set

  name = dirg+'mpqa_spa'+str(k)+'.pkl.gz' 
  f = gzip.open(name,'wb')
  cPickle.dump(dataset, f, protocol=2)
  f.close()
