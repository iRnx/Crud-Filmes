create table distribuidores(
id int auto_increment primary key not null,
nome varchar(50) not null unique
);

create table classificacao(
id int auto_increment primary key not null,
idade int not null
);

create table genero(
id int auto_increment primary key not null,
nome varchar(50) not null unique
);

create table filmes(
id int primary key auto_increment not null,
nome varchar(60) not null unique,
ano int not null,
id_distribuidor int not null,
id_genero int not null,
id_classificacao int not null,
foreign key(id_distribuidor) references distribuidores(id),
foreign key(id_genero) references genero(id),
foreign key(id_classificacao) references classificacao(id)
);

insert into distribuidores (nome) values ('Fox Film'); # id 1

insert into classificacao (idade) values ('12 Anos'); # id 1

insert into genero (nome) values ('Comédia'); # id 1


select * from distribuidores order by id desc;
select * from classificacao order by idade;
select * from genero order by id desc;
select * from filmes;

select f.nome, f.ano, d.nome as 'Distribuidor', g.nome as 'Gênero', c.idade as 'Classificação Indicativa'
from filmes as f, distribuidores as d, genero as g, classificacao as c
where f.id_distribuidor = d.id and f.id_genero = g.id and f.id_classificacao = c.id;







