package main

import "io/ioutil"

type Pagina struct {
	Titulo string
	Corpo  []byte
}

func (p *Pagina) salvar() error{
	nomeDoArquivo := p.Titulo + ".txt"
	return ioutil.WriteFile(nomeDoArquivo, p.Corpo, 0600)

}


func main() {

}