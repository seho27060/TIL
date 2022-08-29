package com.practice.prac1.Domain.DTO;

import com.practice.prac1.Domain.Member;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.Optional;

@Getter
@Builder
public class MemberResDTO {
    private Long id;
    private String name;
}
