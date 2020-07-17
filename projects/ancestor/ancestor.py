from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):

    q = Queue()

    path = [starting_node]

    q.enqueue(path)

    while q.size() > 0:
        currentPath = q.dequeue()
        newPath = []
        changed = False

        for node in currentPath:
            for ancestor in ancestors:
                if ancestor[1] == node:

                    newPath.append(ancestor[0])

                    changed = True

                    q.enqueue(newPath)

        if changed is False:
            if currentPath[0] == starting_node:
                return -1

            else:
                return currentPath[0]