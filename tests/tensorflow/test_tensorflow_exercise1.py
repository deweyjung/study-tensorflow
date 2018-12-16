# 20181207 lecture 5-2
# classfication : 특별히 두개 중에 하나를 선택 예측...
# sigmoid logistic function 0 || 1 : 1 / 1+ e^(-W^tX)
import tensorflow as tf


### decode_csv

filename_queue = tf.train.string_input_producer(["StudentsPerformance.csv"])
reader = tf.TextLineReader(skip_header_lines=0)
key, value = reader.read(filename_queue)
#
record_default = [[0.], [""], [""], [""], [""], [0.], [0.], [0.]]
#
c1, c2, c3, c4, c5, c6, c7, c8 = tf.decode_csv(value, record_defaults=record_default)






###



x_data = [[1,2], [2,3], [3,1], [4,3], [5,3], [6,2]]
y_data = [[0], [0], [0], [1], [1], [1]]

X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
# hypothesis = tf.div(1., 1. + tf.exp(tf.matmul(X, W) + b))

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1- hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, cost_val)

    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})

    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)

