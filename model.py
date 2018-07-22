import tensorflow as tf

def bi_rnn_seg_model(tokens, vocab_size, embed_size, dropout):

    # Char Embedding layer
    char_embedding_matrix = tf.Variable(tf.random_uniform([vocab_size, embed_size], -1.0, 1.0))
    char_embedding_matrix = tf.nn.dropout(char_embedding_matrix, keep_prob=self.embedding_dropout, 
                                     noise_shape=[self.vocab_size,1])
    char_embedding_vectors = tf.nn.embedding_lookup(char_embedding_weights, tokens)



    # Bidiraction RNN layer 1
    gru_cell_1 = tf.nn.rnn_cell.GRUCell(embed_size)
    gru_cell_1 = tf.nn.rnn_cell.DropoutWrapper(cell, output_keep_prob=1-dropout)

    (forward_output, backward_output), _ = tf.nn.bidirectional_dynamic_rnn(gru_cell_1, gru_cell_1,
                                            inputs=char_embedding_vectors,
                                            sequence_length=lengths, dtype=tf.float32)

    outputs = tf.concat([forward_output, backward_output], axis=2)
    softmax = tf.nn.softmax(outputs)

    # Word Embedding layer
    word_embedding_weights = tf.Variable(tf.random_uniform([vocabulary_size, state_size], -1.0, 1.0))
    word_embedding_vectors = tf.nn.embedding_lookup(embedding_weights, word_tokens)

    # Bidiraction RNN layer
    gru_cell_2 = tf.nn.rnn_cell.GRUCell(state_size)
    gru_cell_2 = tf.nn.rnn_cell.DropoutWrapper(cell, output_keep_prob=1-dropout)

    (forward_output, backward_output), _ = tf.nn.bidirectional_dynamic_rnn(cell, cell, inputs=embedding_vectors,
                                            sequence_length=lengths, dtype=tf.float32)
    outputs = tf.concat([forward_output, backward_output], axis=2)
