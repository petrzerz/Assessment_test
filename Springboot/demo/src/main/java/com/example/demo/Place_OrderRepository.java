package com.example.demo;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface Place_OrderRepository extends CrudRepository<Place_Order,Long> {

}


