def build_set(filename):
    # A set stores a collection of unique items.  Both adding items and searching for them
    # are quick, so it's perfect for this application.
    found = set()

    with open(filename) as f:
        for line in f:
            # [:2] gives us the first two elements of the list.
            # Tuples, unlike lists, cannot be changed, which is a requirement for anything
            # being stored in a set.
            found.add(tuple(sorted(line.split())))

    return found

set_more = build_set('lovecraft')
set_del = build_set('words')

with open('results.txt', 'w') as out_file:
   # Using with to open files ensures that they are properly closed, even if the code
   # raises an exception.

   for res in (set_more - set_del):
      # The - computes the elements in set_more not in set_del.

      out_file.write(" ".join(res) + "\n")   