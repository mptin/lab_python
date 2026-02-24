def gen_bin_tree(root: int, height: int, left_function=lambda x: x * 3, right_function=lambda x: x + 4) -> dict:
    '''Построение бинарного дерева по заданным корню, высоте'''


    def building(current_height: int, current_root: int) -> dict:
        '''Рекурсия для построения дерева'''
        if current_height <= 0:
            return None
        # Вычисляем потомков по заданным формулам

        left_value = left_function(current_root)
        right_value = right_function(current_root)

        # Рекурсивно строим левое и правое поддеревья
        left_subtree = building(current_height - 1, left_value)
        right_subtree = building(current_height - 1, right_value)

        # Формируем общую ветку
        branch = {'root': current_root}
        if left_subtree is not None:
            branch['left'] = left_subtree
        if right_subtree is not None:
            branch['right'] = right_subtree

        return branch

    return building(height, root)


print(gen_bin_tree(2,6))


