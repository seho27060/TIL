package com.ssafy.specificPJ.Domain;

import com.ssafy.specificPJ.Domain.DTO.MRDTO;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.List;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private int age;

    private String description;

    @OneToMany(mappedBy = "member", cascade =CascadeType.REMOVE)
    private List<Challenge> challengeList;

    public void updateMember(MRDTO member){
        this.age = member.getAge();
        this.description = member.getDescription();
        this.name = member.getName();
    }
}
