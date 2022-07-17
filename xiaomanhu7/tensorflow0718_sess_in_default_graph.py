import tensorflow as tf



# 構建一個session
with tf.compat.v1.Session() as sess:
    
    # 構建一個計算圖
    a = tf.constant([1.0, 2.0])
    b = tf.constant([3.0, 4.0])
    c = a*b
    
    # 把計算圖放到session裡 並運行得到結果
    #print(sess.run(c))
    print(sess.run(c))
    sess.close()
    
