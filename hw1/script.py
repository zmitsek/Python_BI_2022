ddna2dna = {
    'A': 'T',
    'a': 't',
    'T': 'A',
    't': 'a',
    'G': 'C',
    'g': 'c',
    'C': 'G',
    'c': 'g',
}
rna2rna ={
    'A': 'U',
    'a': 'u',
    'U': 'A',
    'u': 'a',
    'G': 'C',
    'g': 'c',
    'C': 'G',
    'c': 'g',
}
dna2rna = {
    'A': 'A',
    'a': 'a',
    'T': 'U',
    't': 'u',
    'G': 'G',
    'g': 'g',
    'C': 'C',
    'c': 'c'
}


while True:
    print('Enter command:', end = ' ')
    command = input()

    if command == 'transcribe':
        print('Enter sequence:', end = ' ')
        dna_matrix = list(input())
        rna = ''
        i = 0
        while i in range(len(dna_matrix)):       # проверяем последовательность на кошерность, если элемент соответствует
            if dna_matrix[i]  in 'AaCcGgTt':     # нуклеотиду, то встраиваем в отоговую последовательность
                rna += dna2rna[dna_matrix[i]]
                i += 1
            else:                                     # при первом же несовпадении - начинаем всё сначала
                print('Invalid alphabet. Try again!')
                print('Enter sequence:', end = ' ')
                rna = ''
                dna_matrix = list(input())
                i = 0
                continue
        print(rna)

    if command == 'reverse':
        print('Enter sequence:', end = ' ')
        sequence = input()
        i = 0
        U = False
        T = False
        while i in range(len(sequence)):      # здесь следующий алгоритм - сначала мы проверяем все нуклеотиды в
            if sequence[i]  in 'AaCcGgTtUu':  # последовательности, затем записываем входную строку в обратном порядке
                if sequence[i] in 'Uu':
                    U = True
                elif sequence[i] in 'Tt':
                    T = True
                i += 1
                if U == T == True:
                    print('Invalid sequence. Thymine can not be in the same sequence as uracil. Try again!')
                    print('Enter sequence:', end = ' ')
                    U = T = False
                    i = 0
                    sequence = input()
                    continue
            else:
                print('Invalid alphabet. Try again!')
                print('Enter sequence:', end = ' ')
                U = T = False
                i = 0
                sequence = input()
                continue                        # всё выше - проверка
        print(sequence[::-1])                   # непосредственно преобразование и вывод результата

    if command == 'complement':
        print('Enter sequence:', end = ' ')
        strand1 = list(input())
        strand2 = ''
        i = 0
        U = False
        T = False
        while i in range(len(strand1)):        # так же, как и в reverse - проверяем каждый элемент на кошерность
            if strand1[i]  in 'AaCcGgTtUu':    # и только затем преобразуем и выводим
                if strand1[i] in 'Uu':
                    U = True
                elif strand1[i] in 'Tt':
                    T = True
                i += 1
                if U == T == True:
                    print('Invalid sequence. Thymine can not be in the same sequence as uracil. Try again!')
                    print('Enter sequence:', end = ' ')
                    i = 0                      # после каждого неправильного элемента обнуляем счётчик и "флаги",
                    U = T = False              # чтобы не было влияния предыдущих неправильных последовательностей
                    strand1 = list(input())
                    continue
            else:
                print('Invalid alphabet. Try again!')
                print('Enter sequence:', end = ' ')
                i = 0
                U = T = False
                strand1 = list(input())
                continue
        if U == True:                         # так как эта команда работает как с ДНК, так и с РНК, то учитываем это
            for i in range(len(strand1)):     # используя разные словари при получении ответа
                strand2 += rna2rna[strand1[i]]
        else:                                  # если в последовательности нет урацила Uu и тимина Tt, по умолчанию считаем,
            for i in range(len(strand1)):      # что это ДНК, напр. CpG-островки находятся в промоторах, и данные
                strand2 += dna2dna[strand1[i]] # последовательности обычно имеют функциональное значение в цепочке ДНК
        print(strand2)

    if command == 'reverse complement':
        print('Enter sequence:', end = ' ')
        straight_seq = input()
        complement_seq = ''
        i = 0
        U = False
        T = False
        while i in range(len(straight_seq)):
            if straight_seq[i]  in 'AaCcGgTtUu':
                if straight_seq[i] in 'Uu':
                    U = True
                elif straight_seq[i] in 'Tt':
                    T = True
                i += 1
                if U == T == True:
                    print('Invalid sequence. Thymine can not be in the same sequence as uracil. Try again!')
                    print('Enter sequence:', end = ' ')
                    U = T = False
                    i = 0
                    straight_seq = input()
                    continue
            else:
                print('Invalid alphabet. Try again!')
                print('Enter sequence:', end = ' ')
                U = T = False
                i = 0
                straight_seq = input()
                continue
        if U == True:
            for i in range(len(straight_seq)):
                complement_seq += rna2rna[straight_seq[i]]
        else:
            for i in range(len(straight_seq)):
                complement_seq += dna2dna[straight_seq[i]]
        print(complement_seq[::-1])
    if command == 'exit':
        print('Good luck')
        break
