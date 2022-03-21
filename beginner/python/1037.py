num = gets.to_f

if num >= 0 and num <= 25.0000
	puts"Intervalo [0,25]"
    elsif num>25.0000 and num <= 50.0000
	puts"Intervalo (25,50]"
    elsif num>50.0000 and num <= 75.0000
	puts"Intervalo (50,75]"
    elsif num>75.0000 and num <= 100.0000
	puts"Intervalo (75,100]"
    else
	puts"Fora de intervalo"
end   
