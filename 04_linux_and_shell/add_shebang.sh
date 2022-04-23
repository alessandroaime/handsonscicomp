#!/bin/bash

for i in "$@"; do
  if ! [[ "`head -1 $i`" == *"#!/bin/bash"* ]]
  then
    echo -e "#!/bin/bash\n$(cat $i)" > $i
  fi
done
