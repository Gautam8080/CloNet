import tensorflow as tf
i=0
for example in tf.python_io.tf_record_iterator("test.tfrecord"):
    result = tf.train.Example.FromString(example)
    print(result, "\n ################################################### \n")
    break
