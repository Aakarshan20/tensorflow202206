import tensorflow as tf
g1 = tf.Graph()

with g1.as_default():
    c1 = tf.constant([1.0])
    
with tf.Graph().as_default() as g2:
    c2 = tf.constant([2.0])

with tf.compat.v1.Session(graph=g1) as sess1:
    print(sess1.run(c1))

with tf.compat.v1.Session(graph=g2) as sess2:
    print(sess2.run(c2))
    
