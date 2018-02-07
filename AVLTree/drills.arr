data Animal:
  | dog(age :: Number, name :: String)
  | bird(name :: String)
end



data NumList:
  | nl-link(first :: Number , rest :: NumList)
  | nl-empty
end

fun contains-3(l :: NumList)-> Boolean:
  cases(NumList) l:
    |nl-empty => false
    |nl-link(f,r) =>
      if f == 3:
        true
      else:
        contains-3(r)
      end
  end
end


fun friends(animal :: Animal, friend :: Animal) -> String:
  cases(Animal) animal:
    | dog(a,n) =>
      cases(Animal) friend:
        | dog(a2,n2) => n + " and " + n2 + " are friends"
        | bird(n2) => "cant be friends"
      end
    | bird(n) => "cant be friends"
  end
end

fun friends2(animal :: Animal, friend :: Animal) -> String:
  if is-dog(animal) and is-dog(friend):
    animal.name + " and " + friend.name + " are friends"
  else:
    "cant be friends"
  end
end

fun addThree(n :: Number) -> Number:
  n + 3
end

fun adderMaker(n :: Number) -> (Number->Number):
  lam(m :: Number): m + n end
end



check:
  friends(dog(10,"a"), dog(10,"b")) is "a and b are friends"
  friends(dog(10,"a"), bird("a")) is "cant be friends"
  n1 = nl-link(5,nl-link(6,nl-link(3,nl-empty)))
  contains-3(n1) is true
  contains-3(nl-link(5,nl-link(6,nl-link(4,nl-empty)))) is false
  contains-3(nl-empty) is false
end